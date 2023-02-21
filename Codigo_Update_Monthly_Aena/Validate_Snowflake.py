import snowflake.connector

def validate():
    # Gets the version
    ctx = snowflake.connector.connect(
        user='DATA_SCIENTIST',
        password='FX0nCgiGg2ErhS7FCaPQkU1GeF7nAenIDsFNo4W1aYfpAloaEvphIkQj21PPrSme',
        account='satocan.eu-west-1'
        )
    cs = ctx.cursor()
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print(one_row[0])
    finally:
        cs.close()
    ctx.close()