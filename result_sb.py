import numpy as np
import cgi, cgitb
from tempfile import TemporaryFile
data = TemporaryFile()

cgitb.enable()
form = cgi.FieldStorage()

def nonlin(x):
	return 1/(1+np.exp(-x))

t = float(form.getvalue("t"))
e = float(form.getvalue("e"))
m = float(form.getvalue("m"))
p = float(form.getvalue("p"))
c = float(form.getvalue("c"))
cb = float(form.getvalue("cb"))

# Only needed here to simulate closing & reopening file
arr = np.load('data_sb.npz')

m = np.array([t,e,m,p,c,cb])

l1 = nonlin(np.dot(m,arr['syn0']))
l2 = nonlin(np.dot(l1,arr['syn1']))

print('Content-Type: text/html')
print('')
print ('''<html>
   <link rel="stylesheet" href="css/form.css">.
    <!--<script type='text/javascript'>
		function close_window()
	{		
		window.close();
    }
	</script>
  -->
<body>
<div class="container">  
  <form id="contact" >
    <h3>Result is </h3>
    <h4>your mark will be %d <br/> thanks for using the algorithm if possible try to give us more data so that we can give more accruate results 
	<br/> 
	</h4>
	<fieldset>  
	  <button name="submit" type="submit" id="contact-submit" data-submit="...Sending" onclick="window.close();">close</button>
    </fieldset>
  </form>
</div>
<body>
<html>'''%(l2*1200))
