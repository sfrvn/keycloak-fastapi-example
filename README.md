## Установка и запуск Keycloak
1. Создать **.env**-файл: `cp local.example.env .env`
2. Запустить контейнеры: `docker compose -f local-docker-compose.yml up -d`
3. Перейти на `:8080`. Совершить вход, используя значения `KC_BOOTSTRAP_ADMIN_USERNAME`, `KC_BOOTSTRAP_ADMIN_PASSWORD`


## Импорт Realm
1. В дропдауне [в левом верхнем углу] нажать *Create realm*
2. Вставить файл `realm-config.json` или его содержимое.
Будет создан `AimSsoRealm` с выставленными настройками, клиентами, группами и пользователями


## Настройка клиента
1. В дропдауне [в левом верхнем углу] выбрать нужный realm (*AimSsoRealm*)
2. Во вкладке *Clients* выбрать/создать нужный клиент
3. Во вкладке *Credentials* клиента нажать *Regenerate* и скопировать ключ
4. Использовать ключ в качествe `client secret` в репозитории клиента


## Экспорт Realm

1. Выполнить экспорт через терминал или панель администратора
**В терминале**. Находясь в директории `keycloak`, выполнить
`sudo bin/kc.sh export --realm <realm name> --file realm-export.json`
(Для экспорта в директорию / экспорта без пользователей etc. использовать ключи из [документации](https://www.keycloak.org/server/importExport#_exporting_a_realm_to_a_file))
**Через GUI**.  Настройки Realm - Дродаун *Action* [в правом верхнем углу] - *Partial export*
2. В финальном JSON-файле необходимо удалить параметр `authorizationSettings`, чтобы избежать конфликтов при последующем импорте


## Запуск FastAPI
`poetry run uvicorn main:app --reload`
