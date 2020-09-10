### Oracle SODA for Python
Simple Oracle Document Access (SODA) set of APIs that allow you to create collection of documents in Oracle Database, so that later you can retrieve/query those documents. Using SODA implementation you can perform CRUD (create,read,update,delete) on documents. Document can be of any MIME type, in this blog we will focus on JSON.
<br>
<br>
There are separate SODA implementations available for languages like Java, Python, PL/SQL & C etc. however SODA for REST can be accessed from all those languages which support REST framework. Refer Oracle documentation for other implementation.
<br>
We will see how we can store/retrieve/filter JSON document in Oracle Database using Python. Oracle Database supports storing and querying JSON data natively.
<br>
__Prerequisite__: Oracle Client 18.3 or higher, Oracle Database 18.1 or higher required for SODA. After that assign SODA_APP role to the database user in which you are going to create SODA collections.
<br>
Refer this [blog](https://bigdataenthusiast.wordpress.com/2020/09/06/oracle-soda-for-python/) for more details. 
