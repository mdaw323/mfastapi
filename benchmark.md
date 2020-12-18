# Benchmark of heroku app deployed to https://mfastapi.herokuapp.com/

## Summary

| requests | concurrency | tpr (mean in ms) |  req/s |
| :------: | :---------: | ---------------: | -----: |
|    1     |      1      |          479.310 |   2.09 |
|   100    |      1      |          545.299 |   1.83 |
|   100    |     10      |          483.559 |  20.68 |
|   100    |     100     |          941.676 | 106.19 |
|   1000   |     100     |          593.204 | 168.58 |

## Test 1: requests: 1 concurrency: 1

```ApacheBench
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking mfastapi.herokuapp.com (be patient).....done


Server Software:        uvicorn
Server Hostname:        mfastapi.herokuapp.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        mfastapi.herokuapp.com

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      1
Time taken for tests:   0.479 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      185 bytes
HTML transferred:       25 bytes
Requests per second:    2.09 [#/sec] (mean)
Time per request:       479.310 [ms] (mean)
Time per request:       479.310 [ms] (mean, across all concurrent requests)
Transfer rate:          0.38 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      282  282   0.0    282     282
Processing:   197  197   0.0    197     197
Waiting:      196  196   0.0    196     196
Total:        479  479   0.0    479     479
```

## Test 2: requests: 100 concurrency: 1

```ApacheBench
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking mfastapi.herokuapp.com (be patient).....done


Server Software:        uvicorn
Server Hostname:        mfastapi.herokuapp.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        mfastapi.herokuapp.com

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      1
Time taken for tests:   54.530 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      18500 bytes
HTML transferred:       2500 bytes
Requests per second:    1.83 [#/sec] (mean)
Time per request:       545.299 [ms] (mean)
Time per request:       545.299 [ms] (mean, across all concurrent requests)
Transfer rate:          0.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      248  394 101.7    405     906
Processing:    83  151  46.0    134     242
Waiting:       83  150  46.4    134     241
Total:        354  545 134.0    520    1112

Percentage of the requests served within a certain time (ms)
  50%    520
  66%    613
  75%    615
  80%    646
  90%    716
  95%    798
  98%    819
  99%   1112
 100%   1112 (longest request)
```

## Test 3: requests: 100 concurrency: 10

```ApacheBench
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking mfastapi.herokuapp.com (be patient).....done


Server Software:        uvicorn
Server Hostname:        mfastapi.herokuapp.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        mfastapi.herokuapp.com

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      10
Time taken for tests:   4.836 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      18500 bytes
HTML transferred:       2500 bytes
Requests per second:    20.68 [#/sec] (mean)
Time per request:       483.559 [ms] (mean)
Time per request:       48.356 [ms] (mean, across all concurrent requests)
Transfer rate:          3.74 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      169  306  61.6    300     458
Processing:    62  105  17.2    105     206
Waiting:       61  104  17.1    105     205
Total:        231  411  75.6    406     664

Percentage of the requests served within a certain time (ms)
  50%    406
  66%    429
  75%    452
  80%    460
  90%    539
  95%    564
  98%    572
  99%    664
 100%    664 (longest request)
```

## Test 4: requests: 100 concurrency: 100

```ApacheBench
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking mfastapi.herokuapp.com (be patient).....done


Server Software:        uvicorn
Server Hostname:        mfastapi.herokuapp.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        mfastapi.herokuapp.com

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      100
Time taken for tests:   0.942 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      18500 bytes
HTML transferred:       2500 bytes
Requests per second:    106.19 [#/sec] (mean)
Time per request:       941.676 [ms] (mean)
Time per request:       9.417 [ms] (mean, across all concurrent requests)
Transfer rate:          19.19 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      265  353  44.3    339     439
Processing:    90  128  17.1    127     162
Waiting:       90  127  17.0    125     161
Total:        355  482  48.1    478     573

Percentage of the requests served within a certain time (ms)
  50%    478
  66%    491
  75%    507
  80%    514
  90%    559
  95%    562
  98%    570
  99%    573
 100%    573 (longest request)
```

## Test 5: requests: 1000 concurrency: 100

```ApacheBench
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking mfastapi.herokuapp.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        uvicorn
Server Hostname:        mfastapi.herokuapp.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        mfastapi.herokuapp.com

Document Path:          /
Document Length:        25 bytes

Concurrency Level:      100
Time taken for tests:   5.932 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      185000 bytes
HTML transferred:       25000 bytes
Requests per second:    168.58 [#/sec] (mean)
Time per request:       593.204 [ms] (mean)
Time per request:       5.932 [ms] (mean, across all concurrent requests)
Transfer rate:          30.46 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      204  378  91.7    370    1034
Processing:    71  108  23.6    105     571
Waiting:       70  105  21.1    103     571
Total:        276  486  98.3    478    1163

Percentage of the requests served within a certain time (ms)
  50%    478
  66%    498
  75%    514
  80%    522
  90%    546
  95%    567
  98%    795
  99%   1085
 100%   1163 (longest request)
```
