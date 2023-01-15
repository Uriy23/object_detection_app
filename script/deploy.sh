#!/usr/bin/env bash
echo " - Deployed branch: $(git branch --show-current)"
export HOST="51.250.81.158"
export APP_PATH="/deploy/object_detection_app"

rsync -e "ssh -o StrictHostKeyChecking=no" \
      --progress -azhr \
      --exclude ".git/*" \
      --exclude "tmp/" \
      . deploy@$HOST:$APP_PATH

ssh deploy@$HOST "\
  ln -sf $APP_PATH/docker-compose.yml $APP_PATH/docker-compose.yml \
  && cd $APP_PATH \
  && docker-compose build \
  && docker-compose up -d \
  && docker system prune --force"
