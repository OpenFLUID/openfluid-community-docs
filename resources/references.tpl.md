{% macro buildlink(url="",pdf="") -%}
{% if url %}
&nbsp;&nbsp;**<a href="{{ url }}" target=_blank>&raquo; View</a>**
{% elif pdf %}
&nbsp;&nbsp;**<a href="http://www.openfluid-project.org/resources/biblio/{{ pdf }}" target=_blank>&raquo; View</a>**
{% endif %}
{%- endmacro %}

## Citing OpenFLUID

If you wish to cite OpenFLUID, please use the following reference:

* {{ CitingRef.author }} {{ CitingRef.title }}. _{{ CitingRef.booktitle }}_.{{ buildlink(CitingRef.link,CitingRef.pdf) }}

BibTex entry:
```tex
{{ CitingBib }}
```


## Publications

### Articles
{% for item in Refsarticle %}
* {{ item.author }}, {{ item.year }}. {{ item.title }}. _{{ item.journal }}_, {{ item.volume }}{% if item.pages %}, {{ item.pages }}{% endif %}.{{ buildlink(item.link,item.pdf) }}
{% endfor %}

### Communications
{% for item in  Refsinproceedings %}
* {{ item.author }}, {{ item.year }}. {{ item.title }}. _{{ item.booktitle }}_, {{ item.address }}.{{ buildlink(item.link,item.pdf) }}
{% endfor %}

### PhD Thesis
{% for item in Refsphdthesis %}
* {{ item.author }}, {{ item.year }}. {{ item.title }}. _{{ item.school }}_.{{ buildlink(item.link,item.pdf) }}
{% endfor %}

### Masters Thesis
{% for item in Refsmastersthesis %}
* {{ item.author }}, {{ item.year }}. {{ item.title }}. _{{ item.school }}_.{{ buildlink(item.link,item.pdf) }}
{% endfor %}

### Reports
{% for item in Refstechreport %}
* {{ item.author }} {{ item.title }}. _{{ item.institution }}_.{{ buildlink(item.link,item.pdf) }}
{% endfor %}
