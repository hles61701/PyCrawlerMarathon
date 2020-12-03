# PyCrawlerMarathon

Scrapy 框架主要處理資料的幾個時機點
  process_item 每個 Item Pipeline 都需要實作，用來檢查資料數據與是否丟棄等決定
  open_spider 當爬蟲開啟時需要處理的流程 (e.g. 檢查資料庫是否可用)
  close_spider 當爬蟲關閉時需要處理的流程 (e.g. 關閉資料庫連線)
