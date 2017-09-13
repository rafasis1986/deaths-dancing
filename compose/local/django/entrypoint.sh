#!/bin sh

set -o errexit
set -o pipefail

cmd="$@"

function database_ready(){
    python << END
    import sys
    import _mysql
    try:
        conn = _mysql.connect(db="$MYSQL_DATABASE", user="$MYSQL_USER", passwd="$MYSQL_PASSWORD", host="db")
    except _mysql_exceptions.OperationalError:
        sys.exit(-1)
    sys.exit(0)
    END
}

until database_ready; do
  >&2 echo "MySql is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySql is up - continuing..."
exec $cmd
