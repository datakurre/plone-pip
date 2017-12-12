import transaction
app.acl_users._doAddUser('admin', 'admin', ['Manager'], [])
transaction.commit()
