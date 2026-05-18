# Binance Futures Testnet Trading Bot

Python-based CLI trading bot for Binance Futures Testnet.

---

# Features

- MARKET Orders
- LIMIT Orders
- STOP LOSS Orders
- BUY and SELL support
- Input validation
- Logging
- Error handling
- Colored CLI output

---

# Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Keys

Create `.env`

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_SECRET_KEY
```

---

# Run MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

# Run LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

# Run STOP LOSS Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type STOP --quantity 0.001 --stopprice 95000
```

---

# Logs

Logs stored in:

```txt
logs/trading_bot.log
```

---

