# Task
Программа предназначена для работы с базой данных, которая хранится в файле db.dat. Она позволяет пользователю вводить новые записи, просматривать все записи, редактировать данные и искать записи по имени. Краткое описание каждой функции:

InputData(): Эта функция запрашивает у пользователя информацию о новой записи, такую как фамилия, имя, отчество, название компании, рабочий и личный телефоны. Затем эта информация сохраняется в файле db.dat.

OutputData(): Эта функция выводит все записи из файла db.dat на экран.

EditData(): Эта функция позволяет пользователю редактировать существующую запись. Пользователь вводит номер строки для редактирования, а затем запрашивается информация для каждого поля. Если пользователь хочет оставить поле без изменений, он может ввести $. Затем измененная информация сохраняется обратно в файл db.dat.

FindDataByName(): Эта функция позволяет пользователю искать записи по имени. Пользователь вводит имя для поиска, а затем функция выводит все записи, содержащие это имя.

Главный цикл программы предлагает пользователю выбрать одну из четырех опций: ввести новую запись, показать все записи, отредактировать данные или найти запись по имени. Затем вызывается соответствующая функция в зависимости от выбора пользователя.
