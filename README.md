# playground-evedata-aws-cdk

after watching [aws cdk intro](https://www.youtube.com/watch?v=ZWCvNFUN-sU) i was really interested in cdk...

this repo contains my first run with aws-cdk to create a simple infrastructure stack.

####  cdk stack will create:
- one ec2 instance to compute eve online market data (no-source) 
- mysql rds instance for static data (eve online sde)
- elasticsearch to store and present market orders and trade posibilities

### initialise the first and empty stack:
```
npm install -g aws-cdk
cdk --version
mkdir playground-evedata-aws-cdk
cd playground-evedata-aws-cdk/
cdk init
cdk init --language python sample-app
```

### prepare the content from this repo:
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### files to look at:
- [setup.py](https://github.com/garmann/playground_evedata_aws_cdk/setup.py)
- [app.py](https://github.com/garmann/playground_evedata_aws_cdk/app.py)
- [playground_evedata_aws_cdk_stack.py](https://github.com/garmann/playground_evedata_aws_cdk/playground_evedata_aws_cdk/playground_evedata_aws_cdk_stack.py)


## planning and open todos:

ec2:
- public instance, ssh key is used
- internals ip from ec2 will be whitelisted on mysql and elasticsearch

mysql:
- rds mysql, very simple deployment, reachable only from ec2 only

elasticsearch:
- elasticsearchdomain with kibana
- reachable from ec2
- reachable from my current public ip
  - can i add parameters into cdk deploy to specify my ip?

notes:
- region = eu-central-1
- default vpc
- evedata source will not exposed in this repo


open todos:
- lookup data from:
  - existing aws services
    - vpcips = names, ids
    - ec2 instances = internal and external ip
  - shell cli parameters
  - env
  - other running stacks?
  - resources created from current cdk stack (metadata?)
- vpc
  - 3 subnets instead of just only two
- rds security group + ingress rule not working yet
  - currently static as plain text
- es domain
  - ip whitelisting automatic + remote home ip as parameter
  - currently static as plain text
- evedata
  - upgrade PyMySQL, SQLAlchemy
  - es listens on port 80, connections string with scheme

example run of trade calculation:
```
[..]
url https://esi.evetech.net/v1/markets/10000002/orders/
x-pages: 314
len: 1236539
(1236539, [])

real	2m54.261s
user	1m2.416s
sys	0m3.274s


(.env) [root@ip-10-0-14-204 evedata]# time python3 trades_jita_buy.py
delete index
create index
(9304, [])
run over orders: 1236539
trades for db 9304
skip counter 1227235

real	8m22.153s
user	2m19.178s
sys	0m12.260s
 ```