<!DOCTYPE html>
<html>
	<meta charset="utf-8">>
<head>
	<title>Json Api.is</title>
	<link rel="stylesheet" type="text/css" href="static/style.css">>
</head>
<body>
	%include('haus.tpl')
	<div class='row'>
		<section>
			<h2>Gengi gjaldmiðla frá Api.is</h2>
			<ul>
				% for i in data['results']:
				<li>
					{{i['shortname']}} {{i['longName']}} - ISKR: {{i['value']}}
				</li>>
				% end
			</ul>>
		</section>
		
	</div>
	%include('fortur.tpl')

</body>
</html>>