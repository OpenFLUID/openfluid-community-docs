{% set currentver = "2.1.10" %}

## Latest version - {{ currentver }}
<div class="docs-main">
  <div class="docs-item">
    <h4>OpenFLUID manual for users<br/>and simulators developers</h4>
    <br/>
     <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ currentver }}/main/html/index.html" target="_blank"><img src="../html.svg"></a>
     <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ currentver }}/main/openfluid_manual_{{ currentver }}.pdf" target="_blank"><img src="../pdf.svg"></a>
  </div>
  <div class="docs-item">
    <h4>ROpenFLUID package<br/>reference manual</h4>
    <br/>
    <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ currentver }}/main/html/index.html" target="_blank"><img src="../html.svg"></a>
    <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ currentver }}/ROpenFLUID/ROpenFLUID-manual.pdf" target="_blank"><img src="../pdf.svg"></a>
  </div>
</div>



## Previous versions

{% for version in ["2.1.9","2.1.8","2.1.7","2.1.6","2.1.5","2.1.4","2.1.3","2.1.2","2.1.1","2.1.0",
                   "2.0.2","2.0.1","2.0.0",] %}
### {{ version }}

* OpenFLUID manual for users and simulators developers : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/main/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/main/openfluid_manual_{{ version }}.pdf" target="_blank">PDF</a>
* ROpenFLUID package reference manual : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/html/index.html" target="_blank">HTML</a> -
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/ROpenFLUID-manual.pdf" target="_blank">PDF</a>
{% endfor %}

{% for version in ["1.7.2",] %}
### {{ version }}

* Quick user manual : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/openfluid_quickuser_en.pdf" target="_blank">PDF</a>
* Guide for developing simulation functions, with API reference : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/api/index.html" target="_blank">HTML</a>
* ROpenFLUID package reference <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/ROpenFLUID-manual.pdf" target="_blank">PDF</a>

{% endfor %}

{% for version in ["1.7.1",] %}
### {{ version }}

* Quick user manual : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/openfluid_quickuser_en.pdf" target="_blank">PDF</a>
* Guide for developing simulation functions, with API reference : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/api/index.html" target="_blank">HTML</a>
{% endfor %}

{% for version in ["1.7.0","1.6.2","1.6.1","1.6.0",] %}
### {{ version }}

* Quick user manual : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/quickuser/openfluid_quickuser_en.pdf" target="_blank">PDF</a>
* Guide for developing simulation functions, with API reference : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/sdk/index.html" target="_blank">HTML</a>
{% endfor %}

{% for version in ["1.5.0","1.4.2","1.4.1","1.4.0",] %}
### {{ version }}

* Quick reference manual : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/{{ version }}/quickref/html/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/{{ version }}/quickref/openfluid-engine_quickref_en.pdf" target="_blank">PDF</a>
* Guide for developing simulation functions, with API reference : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/{{ version }}/sdk/index.html" target="_blank">HTML </a>
{% endfor %}

{% for version in ["1.3",] %}
### {{ version }}.x
* User manual 🇫🇷 : <a href="http://www.openfluid-project.org/resources/docs/manuals/fr/engine/{{ version }}/user/index.html" target="_blank">HTML</a> - 
  <a href="http://www.openfluid-project.org/resources/docs/manuals/fr/engine/{{ version }}/OpenFLUID-Engine_User.pdf" target="_blank">PDF</a>
* Guide for developing simulation functions, with API reference : <a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/{{ version }}/sdk/index.html" target="_blank">HTML</a>
{% endfor %}