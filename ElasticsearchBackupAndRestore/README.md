## Elasticsearch Backup and Restore

- [Shell Script](https://github.com/shams-sam/logic-lab/blob/master/ElasticsearchBackupAndRestore/elastic_command)
- [Environment Variable Config](https://github.com/shams-sam/logic-lab/blob/master/ElasticsearchBackupAndRestore/config.sh)

## Setup
````
for ES version < 2.x: 
  sudo /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.7.1
else: 
  sudo /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws
````
````
1. ls /usr/share/elasticsearch/plugin should show cloud-aws
2. restart the elasticsearch server
3. curl localhost:9200/_nodes/plugin should show cloud-aws
````

## One click backup and restore
````
source config.sh
. elastic_commnd &&  es_backup
. elastic_commnd &&  es_restore
````

## Functions
### General Purpose
````
1. get_arg $1 $2               returns $2 if not empty else $1
2. get_timestamp               gets current time stamp
3. get_memory_usage            gets current memory usage
4. get_disc_usage              gets current disc space usage
````
### Elasticseach Index
````
1. close_index $1              close the index before restore
2. open_index $1               open the index
3. check_index_status $1       checks index status
````
### AWS Cloud Backup Repository
````
1. _repo_exists $1             checks if repo exists
2. get_repo $1                 gets a repo and creates one if not present
3. verify_repo $1              verify the repo is created successfully
4. delete_repo $1              delete the repo if present
````
### AWS Cloud Backup Snapshot
````
1. get_snapshot $1 $2          get all snapshots in the repo
2. get_snapshot_status $1 $2   get snapshot status while backup    
3. create_snapshot $1          create snapshot with given name
4. delete_snapshot $1          delete snapshot with given name
````
### AWS Cloud Backup Restore
````
1. restore_snapshot $1         restore snapshot with given name
2. get_recovery_status $1      check recovery status while restore
````
## [Reference](https://cuongba.com/backup-and-restore-elasticsearch-with-amazon-s3/)
