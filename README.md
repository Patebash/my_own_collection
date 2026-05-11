# Ansible Collection - patebash.my_own_collection

Ansible collection с кастомным модулем и ролью для создания текстовых файлов на хостах.

---

# Описание

Коллекция предназначена для обучения работе с:
- кастомными модулями Ansible
- ролями
- структурой collections
- идемпотентностью

Модуль создаёт или обновляет текстовый файл на целевом хосте.

---

# Состав

- **my_own_module** — модуль для работы с файлами
- **create_test_file** — роль для упрощённого использования модуля
- **tests** — тестовый playbook для роли
- **playbook.yml** - playbook для коллекции

---

# Структура

```text
plugins/modules/my_own_module.py
roles/create_test_file/
tests/test.yml
playbook.yml
galaxy.yml
```

---

# Параметры модуля

| Параметр | Тип | Описание         |
| -------- | --- | ---------------- |
| path     | str | Путь к файлу     |
| content  | str | Содержимое файла |

---

# Пример использования модуля

```yml
- name: Create file
  patebash.my_own_collection.my_own_module:
    path: /tmp/test.txt
    content: "Hello world"
```

---

# Пример использования роли

```yml
- name: Test role
  hosts: localhost
  gather_facts: false

  collections:
    - patebash.my_own_collection

  roles:
    - create_test_file
```

---

# Запуск тестов

```bash
ansible-playbook playbook.yml
```

---

# Поведение модуля

```text
 * создаёт файл, если его нет
 * обновляет, если содержимое изменилось
 * ничего не делает, если данные одинаковые (идемпотентность)
```

---

# Автор

Patebash (@Patebash)
