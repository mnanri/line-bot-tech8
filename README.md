# line-bot-tech8

## Azure <-> LINE Messaging API

- 疎通確認完了
- Azure Function にデプロイ
  - echo program はできる
  - db.json に格納したファイルを読みだす -> 質問に対する回答を抽出 -> 回答を返信

## どこまでやるか問題

- いったん下記で終わらせておく
  > - db.json に格納したファイルを読みだす -> 回答を表示
- 今後の方針
  - 参加者に**このあとどうやってサービスをよくしていくか**を議論してもらう（アイディアソン的な）
  - LINE API を読んでもらってもいいし，自由発想でもよいかなぁ

## 本番用

- 参考サイト
  - https://zenn.dev/mochan_tk/articles/d01a24bb576d18
- `main` branch: カンペ用
- `for-error-handling` branch: 実装用（最低限の`__ini__.py`）
