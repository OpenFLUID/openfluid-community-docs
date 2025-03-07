
## System compatibility matrix
This table show the levels of compatibility between OpenFLUID versions and several operating systems. (Last update: September 2024)

<div class="compatibility-matrix">
  <table class="legend">
    <tr><td class="status-s example">s</td><td class="detail">stands for <b>supported</b>. OpenFLUID can be installed using packages available on the <a href="https://www.openfluid-project.org/downloads/">OpenFLUID website</a>.</td></tr>
    <tr><td class="status-c example">c</td><td class="detail">stands for <b>checked</b>. No package is provided but OpenFLUID can be built manually.</td></tr>
    <tr><td class="status-t example">t</td><td class="detail">stands for <b>should work</b> but was not tested.</td></tr>
    <tr><td class="status-e example">e</td><td class="detail">stands for <b>experimental</b>. Manual adjustments can make OpenFLUID to be built and working.</td></tr>
    <tr><td class="status-x example">x</td><td class="detail">stands for <b>not working</b>. A manual compilation cannot be achieved.</td></tr>
  </table>
</div>


<br/>

{{nativeMatrix}}


## DockerHub versions
Here are listed versions of OpenFLUID Docker images that can be pulled from [DockerHub](https://hub.docker.com/r/openfluid/openfluid) and on which Linux version they are built.

<table class="compatibility-matrix">
<thead>
<tr><th>OpenFLUID version</th><th>Base OS</th>
</thead>
<tr>
{% for i in dockerhubTable %}
<tr>
<td>{{i}}</td>
<td>{{dockerhubTable[i]}}</td>
</tr>
{% endfor %}
</table>