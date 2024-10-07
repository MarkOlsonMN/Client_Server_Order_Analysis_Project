# Client_Server_Order_Analysis_Project  
  
  
# PROJECT OUTLINE ... (so far) ...  
  
  
DEFINE BEHAVIOR
===============  
who - who placed order  
what - types of items ordered  
how many - quantity levels of items ordered  
when - how often , or how sparse, an order is generated  
where - where item delivered to  
kits ... always order item a with item b  
  
  
CLIENT IN  
=========  
uses random generator seed to define behavior  
generate random data using random generator seed  
convert random data into a transaction document - transaction document can be XML or JSON  
send transaction document to server  
database to hold the random data generated  
database to record transaction document was sent to server  
  
request transaction document status updates from server  
database to record transaction document status updates received  
  
  
SERVER IN  
=========  
endpoint to receive transaction document  
endpoint to handle transaction document status updates  
parse transaction document into transaction data  
database to hold transaction data received from client  
database to record transaction document was received by server  
database to record transaction document status updates  
- transaction document status updates are created as the received transaction document is processed by the server

  
-----------------------------------------------------------------------------------------------------  
  
  
SERVER OUT TRANSACTION  
======================  
provides interface to request detailed info about transaction data  
  
  
CLIENT OUT TRANSACTION  
======================  
provides an user interface to define a request  
send request to server  
receives response back from server  
display detailed info about transaction data  
  
  
SERVER OUT ANALYSIS  
===================  
does statistical analysis to determine behavior  
  
  
CLIENT OUT ANALYSIS  
===================  
displays analysis results  
  
