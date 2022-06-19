from model.group import Group
from random import randrange

def test_modify_first_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="rwerwer"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="rwerwer")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(id, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
