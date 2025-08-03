app = Flask(name)

@app.route('/signal', methods=['GET']) def get_signal(): symbol = request.args.get('symbol', 'EURUSD=X') data = yf.download(tickers=symbol, period='1d', interval='1m')

if data.empty or len(data) < 50: 400 return jsonify({'error': 'Not enough data'}),

df = data.copy() df['ema_9'] = ta.trend.ema_indicator(df['Close'], window=9) df['ema_21'] = ta.trend.ema_indicator(df['Close'], window=21) df['rsi'] = ta.momentum.rsi(df['Close'], window=14) macd = ta.trend. MACD (df['Close']) df['macd'] = macd.macd() df['macd_signal'] = macd.macd_signal()

latest = df.iloc[-1]

if latest['ema_9'] > latest['ema_21'] and latest['rsi'] < 70 and latest['macd'] > latest['macd_signal']: signal = "BUY"latest['ema_9'] < latest['ema_21'] and latest['rsi'] > 30 and latest['macd'] < latest['macd_signal']: signal = "SELL" signal = "HOLD"

else:

return jsonify({ }) 'symbol': symbol, 'signal': signal, 'price': round(latest['Close'], 4)

if name == '_main_': app.run()
