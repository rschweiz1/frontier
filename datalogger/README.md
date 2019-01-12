## Query Tool ##
The Query Tool is a Python abstraction of the TD Ameritrade Developer's API. It
supports various commands to interface with it, including getting quotes, posting
orders, and modifying account preferences.

### Command List ###

* Name: '**query**'
* Usage: 'query <subcommand> <subcommand arguments>'
* Subcommands:

   Name: '_quote_'
   Description: Gets a quote for a given market symbol.
   Arguments: [symbol]
   
   Name: '_help_'
   Description: Prints relevant help text.
   Arguments: None
   
   Name: '_quit_'
   Description: Quits the terminal.
   Arguments: None