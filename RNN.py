#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt



# -- Model --
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.rnn(x)
        return self.fc(out[:, -1])





# -- CONFIG --
SEQ_LEN = 10
PRED_COL = 'DHT_Temperature_C'
INPUT_COLS = [
    'BMP_Temperature_C', 'BMP_Pressure_hPa', 'BMP_Altitude_m',
    'DHT_Humidity_percent', 'BH1750_Light_lx'
]
EPOCHS = 100
LR = 1e-3
HIDDEN_SIZE = 32

# -- LOAD DATA --
df = pd.read_csv("cut_data.csv", parse_dates=['Timestamp'])
df = df.dropna()
df = df.sort_values('Timestamp')
df = df.reset_index(drop=True)

# Normalize
scalers = {}
scaled_df = df.copy()
for col in INPUT_COLS + [PRED_COL]:
    scalers[col] = MinMaxScaler()
    scaled_df[col] = scalers[col].fit_transform(df[[col]])

# -- BUILD SEQUENCES --
X, Y = [], []
for i in range(len(scaled_df) - SEQ_LEN):
    seq_x = scaled_df[INPUT_COLS].iloc[i:i+SEQ_LEN].values
    seq_y = scaled_df[PRED_COL].iloc[i+SEQ_LEN]
    X.append(seq_x)
    Y.append(seq_y)

X = np.array(X)
Y = np.array(Y)

# -- Torch Datasets --
X_torch = torch.tensor(X, dtype=torch.float32)
Y_torch = torch.tensor(Y, dtype=torch.float32).unsqueeze(1)



model = SimpleRNN(input_size=len(INPUT_COLS), hidden_size=HIDDEN_SIZE)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LR)

# -- Training loop --
losses = []
for epoch in range(EPOCHS):
    model.train()
    pred = model(X_torch)
    loss = loss_fn(pred, Y_torch)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

# -- Loss Plot --
plt.plot(losses)
plt.title("Training Loss Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.grid(True)
plt.tight_layout()
plt.show()

# -- Prediction (back to real units) --
model.eval()
with torch.no_grad():
    pred = model(X_torch).squeeze().numpy()

real_y = scalers[PRED_COL].inverse_transform(Y.reshape(-1, 1)).squeeze()
pred_y = scalers[PRED_COL].inverse_transform(pred.reshape(-1, 1)).squeeze()

plt.plot(real_y, label="Actual")
plt.plot(pred_y, label="Predicted")
plt.legend()
plt.title("DHT_Temperature_C Prediction")
plt.xlabel("Timestep")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.show()

# -- Forecasting into the future (few days) --
# Assume samples are spaced ~5 sec apart -> 17,280 steps ≈ 1 day
samples_per_day = int(86400 / 5)
forecast_days = 3
steps = forecast_days * samples_per_day

seed = X[-1]
future = []

for _ in range(steps):
    x_in = torch.tensor(seed, dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        next_pred = model(x_in).item()

    # De-normalize prediction
    real_pred = scalers[PRED_COL].inverse_transform([[next_pred]])[0][0]
    future.append(real_pred)

    # Build new input window
    new_row = seed[1:].tolist()
    last_input = scaled_df[INPUT_COLS].iloc[-1].tolist()
    new_row.append(last_input)
    seed = np.array(new_row)

# -- Plot forecast
plt.plot(future, label="Future Forecast")
plt.title(f"Forward Prediction ({forecast_days} days)")
plt.xlabel("Timestep (~5s interval)")
plt.ylabel("Temperature (C)")
plt.legend()
plt.tight_layout()
plt.show()