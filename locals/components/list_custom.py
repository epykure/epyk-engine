
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Stepper data
records = []
for i in range(6):
  records.append({'text': 'test %s' % i, 'color': 'red', 'icon': 'fas fa-bolt'})

# Create a bespoke list.
lt = page.ui.lists.items(records)

# This function will allow the definition of new items for the list
lt.add_type("bespoke", '''
var item = document.createElement("DIV"); 

var span = document.createElement("SPAN");  
span.setAttribute('name', 'value'); span.setAttribute('data-valid', true);
span.style.color = data.color;

var icon = document.createElement("I"); 
if(typeof data.icon !== 'undefined') {data.icon.split(" ").forEach(function(s){icon.classList.add(s)})}
icon.style.margin = '2px 5px';

item.appendChild(icon); 
item.appendChild(span); 

if(options.click != null){ 
  item.style.cursor = 'pointer';
  item.onclick = function(event){ var value = this.innerHTML; options.click(event, value) }};
if(typeof data === 'object'){ span.innerHTML = data.text} else { span.innerHTML = data }
''', dependencies=['font-awesome'])
