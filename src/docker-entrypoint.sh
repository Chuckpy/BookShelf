echo "ENTRYPOINT >"

export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}

# Aplly database migrations
echo "Aplly database migrations"
python manage.py makemigrations

echo "Collecting static files"
python3 manage.py collectstatic --noinput

until python manage.py migrate; do
  >&2 echo "Postgres may be unavailable - sleeping"
  sleep 10
done


# Start Server
echo ">>>>>>> Starting server <<<<<<<<"
python manage.py runserver 0.0.0.0:${PORT}