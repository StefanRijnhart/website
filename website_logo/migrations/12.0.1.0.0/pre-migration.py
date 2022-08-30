def migrate(cr, version):
    """ Rename view xml-id """
    if not version:
        return
    cr.execute(
        """
        update ir_model_data
        set name = 'add_logo_to_website'
        where name = 'layout_logo_show'
        and module = 'website_logo';
        """
    )
