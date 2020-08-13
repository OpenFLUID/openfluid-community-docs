
<table class="manuals">
<thead>
<tr>
<th></th>
<th><p>HTML</p></th>
<th><p>PDF</p></th>
</tr>
</thead>
<tbody>
{% for version in ["2.1.10","2.1.9","2.1.8","2.1.7","2.1.6","2.1.5","2.1.4","2.1.3","2.1.2","2.1.1","2.1.0",
                   "2.0.2","2.0.1","2.0.0",] %}
<tr>
  <td><p><b>{% if loop.index == 1 %}<u>{% endif %}v{{ version }}{% if loop.index == 1 %}</u>{% endif %}</b></p></td>
  <td>
    <ul>
      <li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/main/html/index.html">OpenFLUID manual for users and simulators developers</a></li>
      <li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/html/index.html">ROpenFLUID package reference</a></li>
    </ul>
  </td>
  <td>
    <ul>
      <li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/main/openfluid_manual_{{ version }}.pdf">OpenFLUID manual for users and simulators developers</a></li>
      <li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/{{ version }}/ROpenFLUID/ROpenFLUID-manual.pdf">ROpenFLUID package reference</a></li>
    </ul>
  </td>
</tr>
{% endfor %}

<tr>
<td><p><b>v1.7.2</b></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.2/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.2/api/index.html">Guide for developing simulation functions, with API reference</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.2/ROpenFLUID/html/index.html">ROpenFLUID package reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.2/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.2/ROpenFLUID/ROpenFLUID-manual.pdf">ROpenFLUID package reference</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.7.1</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.1/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.1/api/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.1/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.7.0</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.0/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.0/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.7.0/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.6.2</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.2/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.2/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.2/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><B>v1.6.1</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.1/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.1/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.1/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.6.0</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.0/quickuser/html/index.html">Quick user manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.0/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/openfluid/1.6.0/quickuser/openfluid_quickuser_en.pdf">Quick user manual</a></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><B>v1.5.0</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.5.0/quickref/html/index.html">Quick reference manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.5.0/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.5.0/quickref/openfluid-engine_quickref_en.pdf">Quick reference manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.4.2</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.2/quickref/html/index.html">Quick reference manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.2/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.2/quickref/openfluid-engine_quickref_en.pdf">Quick reference manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.4.1</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.1/quickref/html/index.html">Quick reference manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.1/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.1/quickref/openfluid-engine_quickref_en.pdf">Quick reference manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.4.0</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.0/quickref/html/index.html">Quick reference manual</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.0/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.4.0/quickref/openfluid-engine_quickref_en.pdf">Quick reference manual</a></li>
</ul></td>
</tr>
<tr>
<td><p><B>v1.3.x</B></p></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/fr/engine/1.3/user/index.html">User manual (in french)</a></li>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/en/engine/1.3/sdk/index.html">Guide for developing simulation functions, with API reference</a></li>
</ul></td>
<td><ul>
<li><a href="http://www.openfluid-project.org/resources/docs/manuals/fr/engine/1.3/OpenFLUID-Engine_User.pdf">User manual (in french)</a></li>
</ul></td>
</tr>
</tbody>
</table>
