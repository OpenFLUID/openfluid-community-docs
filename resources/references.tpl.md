{% macro buildtitle(title="",url="",pdf="") -%}
{% if url -%}
**<a href="{{ url }}" target=_blank>{{- title -}}</a>**
{%- elif pdf -%}
**<a href="http://www.openfluid-project.org/resources/biblio/{{ pdf }}" target=_blank>{{- title -}}</a>**
{%- else -%}
**{{- title -}}**
{%- endif %}
{%- endmacro %}

## Citing OpenFLUID

If you wish to cite OpenFLUID, please use the following reference:

* {{ CitingRef.author }}, {{ CitingRef.year }}. {{ buildtitle(CitingRef.title,CitingRef.url,CitingRef.pdf) }}. _{{ CitingRef.booktitle }}_.

BibTex entry:
```
{{ CitingBib }}
```

## OpenFLUID references

_The following references are about OpenFLUID itself or about using OpenFLUID as a modelling and simulation platform for scientific applications._

### Articles
{% for item in Refsarticle %}
* {{ item.author }}, {{ item.year }}. {{ buildtitle(item.title,item.link,item.pdf) }}. _{{ item.journal }}_{% if item.volume %}, {{ item.volume }}{% endif %}{% if item.pages %}, {{ item.pages }}{% endif %}.
{% endfor %}

### Communications
{% for item in  Refsinproceedings %}
* {{ item.author }}, {{ item.year }}. {{ buildtitle(item.title,item.link,item.pdf) }}. _{{ item.booktitle }}_, {{ item.address }}.
{% endfor %}

### PhD Thesis
{% for item in Refsphdthesis %}
* {{ item.author }}, {{ item.year }}. {{ buildtitle(item.title,item.link,item.pdf) }}. _{{ item.school }}_.
{% endfor %}

### Master's Thesis
{% for item in Refsmastersthesis %}
* {{ item.author }}, {{ item.year }}. {{ buildtitle(item.title,item.link,item.pdf) }}. _{{ item.school }}_.
{% endfor %}

### Reports
{% for item in Refstechreport %}
* {{ item.author }}, {{ item.year }} {{ buildtitle(item.title,item.link,item.pdf) }}. _{{ item.institution }}_.
{% endfor %}
