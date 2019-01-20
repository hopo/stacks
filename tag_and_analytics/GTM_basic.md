<!-- $theme: gaia -->

# GTM

### \# LIST
+ Variables
+ Triggers
+ Tags

### \# Variables
+ variety Variables
+ using custom JS
	> ex)
	>```javascript
	> function() {return document.querySelector('#searchText');}
	>```

### \# Triggers
+ making for fire

### \# Tags
+ using custom UA
+ using custom HTML
	> ex)
	>```html
	> <script>
    > dl = window.dataLayer || [];
    > dl.push({
    >   'event' : 'searchText',
    >   'searchText' : {
    >     'value' : {{searchText_value}},
    > 	  'count' : 3
    >   }
    > })
	> </script>
	>```

