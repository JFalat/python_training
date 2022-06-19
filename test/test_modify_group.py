from model.group import Group
import random

def test_modify_first_name(app, db, check_ui ):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="rwerwer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

