# django-project
To add data into DB:
$ python3 manage.py shell

    >>> 1. import the model(s) eg 
    >>> from nav.models import ToDoList, Item
    >>> t = ToDoList(name="Hezron List")
    >>> t.save()

    % query the DB
    % 1st method to query the DB
    >>> ToDoList.objects.all()
    % 2nd method to query the DB
    >>> ToDoList.objects.get(id=1)


    % Add Items becoz  or r/ship created
    >>> t.item_set.create(text="Go to the Mall", complete=False)
    >>>  t.item_set.all()

    % FILTER : 
    >>> from nav.models import ToDoList, Item
    >>> t = ToDOList.objects
    >>> t.all()
    >>> t.filter(name__startswith="H")

    # Acces Admin account :
        Create super user
