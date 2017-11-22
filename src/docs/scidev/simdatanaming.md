
## Overall rules for naming

### Allowed characters

The allowed characters for naming simulators and data are

* lower case alphabetic characters (`a` to `z`)
* upper case alphabetic characters (`A` to `Z`)
* digits characters (`0` to `9`)
* dash character (`-`)
* dot character (`.`)
* underscore character (`_`)

Space character or any other character are not allowed


### Domain names

The domain name is the basis for naming simulators and variables. The actual defined domains are the following (not exhaustively listed):

Examples

| Domain | Description |
| --- | --- |
| energy | everything in relation with main sources of energy (e.g. temperature, kinetic energy, radiation ...) |
| eros | everything concerning erosion processes and sediment or solid materials fluxes |
| global | which is generally common to several domains or fluxes compartments (sub-domain) |
| plant | processes or fluxes where plants or organs are considered as the main object |
| pop | for Persistent Organic Pollutant - everything regarding pollutant fluxes and processes (e.g. pesticides) |
| soil | processes or fluxes where the soil (surface or unsaturated zone, or saturated zone) is considered as the main object |
| water | everything regarding water fluxes (either in liquid, or solid or gaz phases) - mainly hydrological simulators |


## Variables name

The names of the variables are built following this given nomemclature: **domain.subdomain.symbol.variablename**

* the parts of the name are in english
* the domain name is shorten (see domain name below), which can be extended with the "zone": water, surf, pop
* the symbol is upper case: V, C, M, ...


Examples

| Variable name | Description
| --- | --- |
| water.surf.V.downstream | value representing downstream water volume |
| water.surf.H.infiltration | value representing infiltrated water height at surface |
| water.surf.H.level-rs | value representing water level in a RS |
| water.surf.Q.downstream-rs | value representing water output stream of a SU |
| pop.surf.C.water | value representing pop concentrations in runoff water (liquid phase) |
| pop.surf.C.sediment | value representing pop concentration in runoff sediments (solid phase) |
| pop.surf.M.residue | value representing pop quantity at surface |
| pop.surf.M.applied | value representing initially applied pop quantity |
| pop.plant.M.dissipated | value representing dissipated pop quantity on plants |
| water.sz-uz.H.recharge | value representing water height recharging groundwater |
| water.surf.H.runoff | value representing runoff at surface |
| water.sz-uz.-.storage-coefficient | value representing storage coefficient |
| eros.diff.M.splash | value representing soil mass detached by splash |
| eros.conc.M.rill | value representing soil mass detached by runoff |
| eros.diff.E.kinetic-rain | value representing kinetic energy of rain |
| eros.diff.E.kinetic-canopy | value representing kinetic energy of rain falling on vegetation |



## Simulators ID

The simulators ID are built following this given nomemclature: **domain.subdomain.process.method**

* the parts of the name are in english
* the domain name is shorten (see domain name below), which can be extended with the "zone": water, surf, pop
* in case of multiple processes modelled by the simulator, they will be separated by a dash (`-`)


Examples

| ID  | Description |
| --- | --- |
| water.surf-uz.runoff-infiltration.mseytoux | runoff-infiltration production using the Morel-Seytoux method |
| water.surf.transfer-su.hayami | water surface transfer on SU using the Hayami method |
| water.surf-uz.flow-su.richards | water transfer in the unsaturated zone on SU using Richards equation |
| water.surf-uz.flow-rs.richards | water transfer in the unsaturated zone on RS using Richards equation |
| water.sz.flow.boussinesq | water transfer in the unsaturated zone on the whole domain using the Boussinesq equation|
