---
slug: test
title: test
authors: timger
tags:
  - sentry
  - docker
---
参考 https://github.com/getsentry/self-hosted

默认安装 docker 和 docker compose 需要前提安装
```bash  
git clone https://github.com/getsentry/self-hosted.git
VERSION="24.1.0"
cd self-hosted
git checkout ${VERSION}
./install.sh
```

日志

```txt
root@dafengstido:/data/riad-data/projects/self-hosted# ./install.sh
▶ Parsing command line ...

▶ Detecting Docker platform
Detected Docker platform is linux/amd64

▶ Initializing Docker Compose ...

▶ Setting up error handling ...
#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile:
#1 transferring dockerfile: 292B done
#1 DONE 0.2s

#2 [internal] load .dockerignore
#2 transferring context: 2B done
#2 DONE 0.2s

#3 [internal] load metadata for docker.io/library/debian:bookworm-slim
#3 DONE 38.7s

#4 [1/2] FROM docker.io/library/debian:bookworm-slim@sha256:67f3931ad8cb1967beec602d8c0506af1e37e8d73c2a0b38b181ec5d8560d395
#4 resolve docker.io/library/debian:bookworm-slim@sha256:67f3931ad8cb1967beec602d8c0506af1e37e8d73c2a0b38b181ec5d8560d395 0.1s done
#4 sha256:84d83b22ba6c367e143fcb7169717d87d7f484356cf9a904f5352418981a99a3 529B / 529B done
#4 sha256:46a63b82e4145c5eb93ce87cb6b3e6eeb89a4318b848b8e44a2ea029ccfdc157 1.46kB / 1.46kB done
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 0.2s
#4 sha256:67f3931ad8cb1967beec602d8c0506af1e37e8d73c2a0b38b181ec5d8560d395 1.85kB / 1.85kB done
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 5.4s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 10.5s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 15.7s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 20.7s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 25.8s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 31.0s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 36.1s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 41.2s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 46.4s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 51.5s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 56.6s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 0B / 29.15MB 61.6s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 3.15MB / 29.15MB 63.5s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 9.44MB / 29.15MB 63.6s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 15.73MB / 29.15MB 63.7s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 29.15MB / 29.15MB 63.9s
#4 sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 29.15MB / 29.15MB 64.3s done
#4 extracting sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44
#4 extracting sha256:2cc3ae149d28a36d28d4eefbae70aaa14a0c9eab588c3790f7979f310b893c44 1.3s done
#4 DONE 66.0s

#5 [2/2] RUN set -x   && apt-get update   && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends jq   && apt-get clean   && rm -rf /var/lib/apt/lists/*
#5 0.276 + apt-get update
#5 0.799 Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
#5 1.423 Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
#5 1.630 Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
#5 1.764 Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8786 kB]
#5 2.400 Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [13.8 kB]
#5 2.523 Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [160 kB]
#5 3.563 Fetched 9214 kB in 3s (2822 kB/s)
#5 3.563 Reading package lists...
#5 4.233 + DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends jq
#5 4.239 Reading package lists...
#5 4.886 Building dependency tree...
#5 5.029 Reading state information...
#5 5.261 The following additional packages will be installed:
#5 5.263   libjq1 libonig5
#5 5.315 The following NEW packages will be installed:
#5 5.317   jq libjq1 libonig5
#5 5.693 0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
#5 5.693 Need to get 388 kB of archives.
#5 5.693 After this operation, 1165 kB of additional disk space will be used.
#5 5.693 Get:1 http://deb.debian.org/debian bookworm/main amd64 libonig5 amd64 6.9.8-1 [188 kB]
#5 5.994 Get:2 http://deb.debian.org/debian bookworm/main amd64 libjq1 amd64 1.6-2.1 [135 kB]
#5 6.021 Get:3 http://deb.debian.org/debian bookworm/main amd64 jq amd64 1.6-2.1 [64.9 kB]
#5 6.230 debconf: delaying package configuration, since apt-utils is not installed
#5 6.256 Fetched 388 kB in 1s (540 kB/s)
#5 6.309 Selecting previously unselected package libonig5:amd64.
(Reading database ... 6090 files and directories currently installed.)
#5 6.315 Preparing to unpack .../libonig5_6.9.8-1_amd64.deb ...
#5 6.342 Unpacking libonig5:amd64 (6.9.8-1) ...
#5 6.499 Selecting previously unselected package libjq1:amd64.
#5 6.501 Preparing to unpack .../libjq1_1.6-2.1_amd64.deb ...
#5 6.514 Unpacking libjq1:amd64 (1.6-2.1) ...
#5 6.606 Selecting previously unselected package jq.
#5 6.609 Preparing to unpack .../archives/jq_1.6-2.1_amd64.deb ...
#5 6.623 Unpacking jq (1.6-2.1) ...
#5 6.765 Setting up libonig5:amd64 (6.9.8-1) ...
#5 6.806 Setting up libjq1:amd64 (1.6-2.1) ...
#5 6.847 Setting up jq (1.6-2.1) ...
#5 6.889 Processing triggers for libc-bin (2.36-9+deb12u7) ...
#5 6.975 + apt-get clean
#5 6.981 + rm -rf /var/lib/apt/lists/auxfiles /var/lib/apt/lists/deb.debian.org_debian-security_dists_bookworm-security_InRelease /var/lib/apt/lists/deb.debian.org_debian-security_dists_bookworm-security_main_binary-amd64_Packages.lz4 /var/lib/apt/lists/deb.debian.org_debian_dists_bookworm-updates_InRelease /var/lib/apt/lists/deb.debian.org_debian_dists_bookworm-updates_main_binary-amd64_Packages.lz4 /var/lib/apt/lists/deb.debian.org_debian_dists_bookworm_InRelease /var/lib/apt/lists/deb.debian.org_debian_dists_bookworm_main_binary-amd64_Packages.lz4 /var/lib/apt/lists/lock /var/lib/apt/lists/partial
#5 DONE 8.3s

#6 exporting to image
#6 exporting layers
#6 exporting layers 0.1s done
#6 writing image sha256:4e173daad957d52f30272e59eb825e3358d0dc4b9db663b62c7d79505b18a32b 0.0s done
#6 naming to docker.io/library/sentry-self-hosted-jq-local 0.0s done
#6 DONE 0.2s

Hey, so ... we would love to automatically find out about issues with your
Sentry instance so that we can improve the product. Turns out there is an app
for that, called Sentry. Would you be willing to let us automatically send data
about your instance upstream to Sentry for development and debugging purposes?

  y / yes / 1
  n / no / 0

(Btw, we send this to our own self-hosted Sentry instance, not to Sentry SaaS,
so that we can be in this together.)

Here's the info we may collect:

  - OS username
  - IP address
  - install log
  - runtime errors
  - performance data

Thirty (30) day retention. No marketing. Privacy policy at sentry.io/privacy.

y or n? y

Thank you. To avoid this prompt in the future, use one of these flags:

  --report-self-hosted-issues
  --no-report-self-hosted-issues

or set the REPORT_SELF_HOSTED_ISSUES environment variable:

  REPORT_SELF_HOSTED_ISSUES=1 to send data
  REPORT_SELF_HOSTED_ISSUES=0 to not send data

latest: Pulling from getsentry/sentry-cli
f7dab3ab2d6e: Pulling fs layer
8bd10b77a777: Pulling fs layer
80aeafe5b1af: Pulling fs layer
e75529525eaf: Pulling fs layer
8be53abe2c79: Pulling fs layer
e75529525eaf: Waiting
8be53abe2c79: Waiting
f7dab3ab2d6e: Downloading
80aeafe5b1af: Verifying Checksum
80aeafe5b1af: Download complete
8bd10b77a777: Verifying Checksum
8bd10b77a777: Download complete
e75529525eaf: Verifying Checksum
e75529525eaf: Download complete
8be53abe2c79: Verifying Checksum
8be53abe2c79: Download complete
latest: Pulling from getsentry/sentry-cli
f7dab3ab2d6e: Pulling fs layer
8bd10b77a777: Pulling fs layer
80aeafe5b1af: Pulling fs layer
e75529525eaf: Pulling fs layer
8be53abe2c79: Pulling fs layer
e75529525eaf: Waiting
8be53abe2c79: Waiting
8bd10b77a777: Download complete
80aeafe5b1af: Verifying Checksum
80aeafe5b1af: Download complete
e75529525eaf: Verifying Checksum
e75529525eaf: Download complete
8be53abe2c79: Verifying Checksum
8be53abe2c79: Download complete
f7dab3ab2d6e: Verifying Checksum
f7dab3ab2d6e: Download complete
f7dab3ab2d6e: Pull complete
8bd10b77a777: Pull complete
80aeafe5b1af: Pull complete
e75529525eaf: Pull complete
8be53abe2c79: Pull complete
Digest: sha256:d9c7c110c97b3c0c17928c4eb94dc6d09f5d67d97f5ccb0bde796c8806b1b8bd
Status: Downloaded newer image for getsentry/sentry-cli:latest
docker.io/getsentry/sentry-cli:latest

▶ Checking for latest commit ... 
skipped

▶ Checking minimum requirements ...
Found Docker version 24.0.2
Found Docker Compose version 2.17.2
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
ec562eabd705: Pulling fs layer
ec562eabd705: Verifying Checksum
ec562eabd705: Download complete
ec562eabd705: Pull complete
Digest: sha256:9ae97d36d26566ff84e8893c64a6dc4fe8ca6d1144bf5b87b2b85a32def253c7
Status: Downloaded newer image for busybox:latest

▶ Turning things off ...

▶ Creating volumes for persistent storage ...
Created sentry-clickhouse.
Created sentry-data.
Created sentry-kafka.
Created sentry-postgres.
Created sentry-redis.
Created sentry-symbolicator.
Created sentry-zookeeper.

▶ Ensuring files from examples ...
Creating sentry/sentry.conf.py ...
Creating sentry/config.yml ...
Creating symbolicator/config.yml ...

▶ Ensuring Relay credentials ...
Creating relay/config.yml ...
 relay Pulling 
 2f44b7a888fa Pulling fs layer 
 2d135ea31366 Pulling fs layer 
 df9a125bf36c Pulling fs layer 
 0002dd73cf34 Pulling fs layer 
 4f4fb700ef54 Pulling fs layer 
 8f8a328b17e6 Pulling fs layer 
 4db52d7baa8a Pulling fs layer 
 2c19e15b20ad Pulling fs layer 
 0002dd73cf34 Waiting 
 8f8a328b17e6 Waiting 
 4f4fb700ef54 Waiting 
 4db52d7baa8a Waiting 
 2c19e15b20ad Waiting 
 2f44b7a888fa Pulling fs layer 
 2d135ea31366 Pulling fs layer 
 df9a125bf36c Pulling fs layer 
 0002dd73cf34 Pulling fs layer 
 0002dd73cf34 Waiting 
 2d135ea31366 Waiting 
 df9a125bf36c Waiting 
 2f44b7a888fa Waiting 
 4f4fb700ef54 Pulling fs layer 
 0002dd73cf34 Waiting 
 4f4fb700ef54 Waiting 
 8f8a328b17e6 Pulling fs layer 
 8f8a328b17e6 Waiting 
 4f4fb700ef54 Waiting 
 2f44b7a888fa Downloading [>                                                  ]  302.3kB/29.13MB
 2f44b7a888fa Downloading [=>                                                 ]  597.2kB/29.13MB
 2f44b7a888fa Downloading [=>                                                 ]  892.1kB/29.13MB
 2f44b7a888fa Downloading [==>                                                ]  1.187MB/29.13MB
 2d135ea31366 Downloading [>                                                  ]  69.77kB/6.672MB
 2f44b7a888fa Downloading [==>                                                ]  1.482MB/29.13MB
 2d135ea31366 Downloading [=>                                                 ]  209.8kB/6.672MB
 2d135ea31366 Downloading [==>                                                ]  278.5kB/6.672MB
 2f44b7a888fa Downloading [===>                                               ]  1.777MB/29.13MB
 2d135ea31366 Downloading [==>                                                ]  360.4kB/6.672MB
 2f44b7a888fa Downloading [===>                                               ]  2.072MB/29.13MB
 2d135ea31366 Downloading [===>                                               ]  442.4kB/6.672MB
 2d135ea31366 Downloading [====>                                              ]  606.2kB/6.672MB
 2f44b7a888fa Downloading [====>                                              ]  2.367MB/29.13MB
 2d135ea31366 Downloading [=====>                                             ]    770kB/6.672MB
 2f44b7a888fa Downloading [====>                                              ]  2.662MB/29.13MB
 2d135ea31366 Downloading [======>                                            ]    852kB/6.672MB
 2f44b7a888fa Downloading [=====>                                             ]  2.957MB/29.13MB
 2d135ea31366 Downloading [=======>                                           ]  1.016MB/6.672MB
 2d135ea31366 Downloading [========>                                          ]  1.098MB/6.672MB
 2f44b7a888fa Downloading [=====>                                             ]  3.251MB/29.13MB
 2d135ea31366 Downloading [========>                                          ]   1.18MB/6.672MB
 2d135ea31366 Downloading [=========>                                         ]  1.262MB/6.672MB
 2f44b7a888fa Downloading [======>                                            ]  3.546MB/29.13MB
 2d135ea31366 Downloading [==========>                                        ]  1.343MB/6.672MB
 2f44b7a888fa Downloading [======>                                            ]  3.841MB/29.13MB
 2d135ea31366 Downloading [===========>                                       ]  1.507MB/6.672MB
 2d135ea31366 Downloading [===========>                                       ]  1.589MB/6.672MB
 2f44b7a888fa Downloading [=======>                                           ]  4.136MB/29.13MB
 2f44b7a888fa Downloading [=======>                                           ]  4.431MB/29.13MB
 2d135ea31366 Downloading [=============>                                     ]  1.835MB/6.672MB
 2f44b7a888fa Downloading [========>                                          ]  4.726MB/29.13MB
 2d135ea31366 Downloading [==============>                                    ]  1.917MB/6.672MB
 2d135ea31366 Downloading [===============>                                   ]  2.081MB/6.672MB
 2f44b7a888fa Downloading [========>                                          ]  5.021MB/29.13MB
 2d135ea31366 Downloading [================>                                  ]  2.245MB/6.672MB
 2d135ea31366 Downloading [=================>                                 ]  2.327MB/6.672MB
 2f44b7a888fa Downloading [=========>                                         ]  5.316MB/29.13MB
 2d135ea31366 Downloading [==================>                                ]   2.49MB/6.672MB
 2f44b7a888fa Downloading [=========>                                         ]  5.611MB/29.13MB
 2d135ea31366 Downloading [===================>                               ]  2.654MB/6.672MB
 2d135ea31366 Downloading [=====================>                             ]  2.818MB/6.672MB
 2f44b7a888fa Downloading [==========>                                        ]  5.906MB/29.13MB
 2d135ea31366 Downloading [=====================>                             ]    2.9MB/6.672MB
 2f44b7a888fa Downloading [==========>                                        ]  6.201MB/29.13MB
 2f44b7a888fa Downloading [===========>                                       ]  6.495MB/29.13MB
 2d135ea31366 Downloading [=======================>                           ]  3.146MB/6.672MB
 2f44b7a888fa Downloading [===========>                                       ]   6.79MB/29.13MB
 2d135ea31366 Downloading [========================>                          ]   3.31MB/6.672MB
 2d135ea31366 Downloading [==========================>                        ]  3.473MB/6.672MB
 2f44b7a888fa Downloading [============>                                      ]  7.085MB/29.13MB
 2d135ea31366 Downloading [===========================>                       ]  3.637MB/6.672MB
 2f44b7a888fa Downloading [============>                                      ]   7.38MB/29.13MB
 2d135ea31366 Downloading [===========================>                       ]  3.719MB/6.672MB
 2f44b7a888fa Downloading [=============>                                     ]  7.675MB/29.13MB
 2d135ea31366 Downloading [=============================>                     ]  3.965MB/6.672MB
 2d135ea31366 Downloading [==============================>                    ]  4.047MB/6.672MB
 2f44b7a888fa Downloading [=============>                                     ]   7.97MB/29.13MB
 2d135ea31366 Downloading [===============================>                   ]  4.211MB/6.672MB
 2f44b7a888fa Downloading [==============>                                    ]  8.265MB/29.13MB
 2d135ea31366 Downloading [================================>                  ]  4.293MB/6.672MB
 2f44b7a888fa Downloading [==============>                                    ]   8.56MB/29.13MB
 2d135ea31366 Downloading [=================================>                 ]  4.456MB/6.672MB
 2f44b7a888fa Downloading [===============>                                   ]  8.855MB/29.13MB
 2d135ea31366 Downloading [==================================>                ]  4.538MB/6.672MB
 2d135ea31366 Downloading [===================================>               ]  4.784MB/6.672MB
 2f44b7a888fa Downloading [===============>                                   ]   9.15MB/29.13MB
 2d135ea31366 Downloading [====================================>              ]  4.866MB/6.672MB
 2f44b7a888fa Downloading [================>                                  ]  9.445MB/29.13MB
 2d135ea31366 Downloading [=====================================>             ]  4.948MB/6.672MB
 2f44b7a888fa Downloading [================>                                  ]  9.739MB/29.13MB
 2d135ea31366 Downloading [======================================>            ]  5.112MB/6.672MB
 2d135ea31366 Downloading [======================================>            ]  5.194MB/6.672MB
 2f44b7a888fa Downloading [=================>                                 ]  10.03MB/29.13MB
 2d135ea31366 Downloading [=======================================>           ]  5.276MB/6.672MB
 2f44b7a888fa Downloading [=================>                                 ]  10.33MB/29.13MB
 2d135ea31366 Downloading [========================================>          ]  5.358MB/6.672MB
 2f44b7a888fa Downloading [==================>                                ]  10.62MB/29.13MB
 2d135ea31366 Downloading [========================================>          ]  5.439MB/6.672MB
 2f44b7a888fa Downloading [==================>                                ]  10.92MB/29.13MB
 2d135ea31366 Downloading [=========================================>         ]  5.603MB/6.672MB
 2f44b7a888fa Downloading [===================>                               ]  11.21MB/29.13MB
 2d135ea31366 Downloading [===========================================>       ]  5.849MB/6.672MB
 2f44b7a888fa Downloading [===================>                               ]  11.51MB/29.13MB
 2d135ea31366 Downloading [============================================>      ]  5.931MB/6.672MB
 2f44b7a888fa Downloading [====================>                              ]   11.8MB/29.13MB
 2f44b7a888fa Downloading [====================>                              ]   12.1MB/29.13MB
 2d135ea31366 Downloading [=============================================>     ]  6.095MB/6.672MB
 2f44b7a888fa Downloading [=====================>                             ]  12.39MB/29.13MB
 2d135ea31366 Downloading [==============================================>    ]  6.259MB/6.672MB
 2f44b7a888fa Downloading [=====================>                             ]  12.69MB/29.13MB
 2d135ea31366 Downloading [================================================>  ]  6.504MB/6.672MB
 2f44b7a888fa Downloading [======================>                            ]  12.98MB/29.13MB
 2d135ea31366 Downloading [=================================================> ]  6.668MB/6.672MB
 2d135ea31366 Verifying Checksum 
 2d135ea31366 Download complete 
 2f44b7a888fa Downloading [======================>                            ]  13.28MB/29.13MB
 2f44b7a888fa Downloading [=======================>                           ]  13.57MB/29.13MB
 2f44b7a888fa Downloading [=======================>                           ]  13.87MB/29.13MB
 2f44b7a888fa Downloading [========================>                          ]  14.16MB/29.13MB
 df9a125bf36c Downloading [==========================>                        ]     574B/1.072kB
 df9a125bf36c Downloading [==================================================>]  1.072kB/1.072kB
 df9a125bf36c Verifying Checksum 
 df9a125bf36c Download complete 
 2f44b7a888fa Downloading [========================>                          ]  14.46MB/29.13MB
 0002dd73cf34 Downloading [==================================================>]     139B/139B
 0002dd73cf34 Download complete 
 2f44b7a888fa Downloading [=========================>                         ]  14.75MB/29.13MB
 2f44b7a888fa Downloading [=========================>                         ]  15.05MB/29.13MB
 2f44b7a888fa Downloading [==========================>                        ]  15.34MB/29.13MB
 2f44b7a888fa Downloading [==========================>                        ]  15.64MB/29.13MB
 4db52d7baa8a Pulling fs layer 
 2c19e15b20ad Pulling fs layer 
 4db52d7baa8a Waiting 
 2c19e15b20ad Waiting 
 2f44b7a888fa Downloading [===========================>                       ]  15.93MB/29.13MB
 2f44b7a888fa Downloading [===========================>                       ]  16.23MB/29.13MB
 4f4fb700ef54 Downloading [==================================================>]      32B/32B
 4f4fb700ef54 Verifying Checksum 
 4f4fb700ef54 Download complete 
 2f44b7a888fa Downloading [============================>                      ]  16.52MB/29.13MB
 2f44b7a888fa Downloading [============================>                      ]  16.82MB/29.13MB
 2f44b7a888fa Downloading [=============================>                     ]  17.11MB/29.13MB
 2f44b7a888fa Downloading [=============================>                     ]  17.41MB/29.13MB
 2f44b7a888fa Downloading [==============================>                    ]   17.7MB/29.13MB
 2f44b7a888fa Downloading [==============================>                    ]     18MB/29.13MB
 2f44b7a888fa Downloading [===============================>                   ]  18.29MB/29.13MB
 8f8a328b17e6 Downloading [>                                                  ]  172.6kB/16.84MB
 2f44b7a888fa Downloading [===============================>                   ]  18.59MB/29.13MB
 2f44b7a888fa Downloading [================================>                  ]  18.88MB/29.13MB
 8f8a328b17e6 Downloading [=>                                                 ]  352.3kB/16.84MB
 2f44b7a888fa Downloading [================================>                  ]  19.18MB/29.13MB
 4db52d7baa8a Downloading [>                                                  ]  531.7kB/147MB
 8f8a328b17e6 Downloading [=>                                                 ]  532.5kB/16.84MB
 2f44b7a888fa Downloading [=================================>                 ]  19.47MB/29.13MB
 8f8a328b17e6 Downloading [==>                                                ]  712.7kB/16.84MB
 2f44b7a888fa Downloading [=================================>                 ]  19.77MB/29.13MB
 4db52d7baa8a Downloading [>                                                  ]  1.072MB/147MB
 2f44b7a888fa Downloading [==================================>                ]  20.06MB/29.13MB
 8f8a328b17e6 Downloading [==>                                                ]  892.9kB/16.84MB
 2f44b7a888fa Downloading [==================================>                ]  20.36MB/29.13MB
 4db52d7baa8a Downloading [>                                                  ]  1.613MB/147MB
 2f44b7a888fa Downloading [===================================>               ]  20.65MB/29.13MB
 2f44b7a888fa Downloading [===================================>               ]  20.95MB/29.13MB
 8f8a328b17e6 Downloading [===>                                               ]  1.073MB/16.84MB
 2f44b7a888fa Downloading [====================================>              ]  21.24MB/29.13MB
 4db52d7baa8a Downloading [>                                                  ]  2.154MB/147MB
 8f8a328b17e6 Downloading [===
```


如果卡主 手动拉取

加上代理

```
export http_proxy=socks5://192.168.6.1:1070
export https_proxy=socks5://192.168.6.1:1070
```
再 手动拉取

```bash
docker pull getsentry/symbolicator:24.1.0
docker pull getsentry/symbolicator:24.1.0
docker pull getsentry/snuba:24.1.0
docker pull getsentry/relay:24.1.0
docker pull getsentry/symbolicator:24.1.0
docker pull getsentry/vroom:24.1.0
```
执行完之后

```bash
docker-compose up -d
```
```

只能说小配置 确实跑不起

```txt
[+] Running 12/34
 ⠹ Container sentry-self-hosted-subscription-consumer-transactions-1            Stopping                                                                                10.2s 
 ⠹ Container sentry-self-hosted-metrics-consumer-1                              Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-profiling-functions-consumer-1            Removed                                                                                  8.7s 
 ⠹ Container sentry-self-hosted-generic-metrics-consumer-1                      Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-profiling-profiles-consumer-1             Removed                                                                                  9.5s 
 ⠙ Container sentry-self-hosted-subscription-consumer-metrics-1                 Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-generic-metrics-counters-consumer-1       Removed                                                                                  6.3s 
 ⠙ Container sentry-self-hosted-ingest-replay-recordings-1                      Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-ingest-profiles-1                               Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-generic-metrics-distributions-consumer-1  Removed                                                                                  7.2s 
 ✔ Container sentry-self-hosted-snuba-issue-occurrence-consumer-1               Removed                                                                                  9.9s 
 ⠙ Container sentry-self-hosted-transactions-consumer-1                         Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-subscription-consumer-events-1                  Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-symbolicator-cleanup-1                          Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-post-process-forwarder-issue-platform-1         Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-post-process-forwarder-errors-1                 Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-attachments-consumer-1                          Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-generic-metrics-sets-consumer-1           Removed                                                                                  7.3s 
 ⠙ Container sentry-self-hosted-billing-metrics-consumer-1                      Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-subscription-consumer-generic-metrics-1         Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-nginx-1                                         Removed                                                                                  0.3s 
 ⠙ Container sentry-self-hosted-ingest-monitors-1                               Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-events-consumer-1                               Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-replays-consumer-1                        Removed                                                                                  9.7s 
 ⠙ Container sentry-self-hosted-sentry-cleanup-1                                Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-worker-1                                        Removed                                                                                  9.5s 
 ✔ Container sentry-self-hosted-snuba-subscription-consumer-metrics-1           Removed                                                                                 10.0s 
 ⠙ Container sentry-self-hosted-ingest-occurrences-1                            Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-snuba-metrics-consumer-1                        Removed                                                                                  6.3s 
 ⠙ Container sentry-self-hosted-cron-1                                          Stopping                                                                                10.2s 
 ⠙ Container sentry-self-hosted-post-process-forwarder-transactions-1           Stopping                                                                                10.2s 
 ✔ Container sentry-self-hosted-geoipupdate-1                                   Removed                                                                                  0.3s 
 ⠙ Container sentry-self-hosted-vroom-cleanup-1                                 Stopping                                                                                10.2s 
 ⠇ Container sentry-self-hosted-relay-1                                         Stopping
```