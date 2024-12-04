Lambda function syntax:

```
lambda arguments:expression
```

Where is it used ?
-> Lamba function is used where it is only used once in your code

# Filter

Filter that can be deployed in Python to filter out the elements that one is in need of.

Yes, you heard that right. There is a specific function in Python known as 'filter()' function or method that enables you to filter out the elements that you need in a list.

# logging

logging is the process of recording messages during the execution of a program to provide

## components of logging
Logger − It is the main entry point that you use to emit log messages. Each logger instance is named and can be configured independently.

Handler − It determines where log messages are sent. Handlers send log messages to different destinations such as the console, files, sockets, etc.

Formatter − It specifies the layout of log messages. Formatters define the structure of log records by specifying which information to include (e.g., timestamp, log level, message).

Logger Level − It defines the severity level of log messages. Messages below this level are ignored. Common levels include DEBUG, INFO, WARNING, ERROR, and CRITICAL.

Filter − It is the optional components that provide finer control over which log records are processed and emitted by a handler.

## levels of logging

DEBUG − Detailed information, typically useful only for debugging purposes. These messages are used to trace the flow of the program and are usually not seen in production environments.

INFO − Confirmation that things are working as expected. These messages provide general information about the progress of the application.

WARNING − Indicates potential issues that do not prevent the program from running but might require attention. These messages can be used to alert developers about unexpected situations.

ERROR − Indicates a more serious problem that prevents a specific function or operation from completing successfully. These messages highlight errors that need immediate attention but do not necessarily terminate the application.

CRITICAL − The most severe level, indicating a critical error that may lead to the termination of the program. These messages are reserved for critical failures that require immediate intervention.


