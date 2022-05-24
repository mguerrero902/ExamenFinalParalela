#!/usr/bin/perl

# Fichero para automatización de ejecución por lotes de un ejecutable
# dado parámetros de entrada.
# $ --> variable
# @ --> vector
$repeticiones = 10;
@ejecutables = ("heat_main");
@data = ("bottle.dat","bottle_medium.dat","bottle_large.dat");
@steps = ("100","200","300","500");
$path = "Your path";#Ingresar su ruta - puede obetenerla ingresando el comando 'pwd' en la terminal
@version =("py","cyt");

foreach $exe (@ejecutables) {
	foreach $dat (@data) {
		foreach $step (@steps){
			
			#print("$fichero\n");
			foreach $ver(@version) {
				$fichero = "$path"."Soluciones/"."$dat"."-steps"."$step"."$ver";
				for ($i=0; $i<$repeticiones; $i++) {
					#print("$path$exe $size\n");
					system("python3 $exe.py -f $dat -n $step -v $ver >> $fichero");
				}
		}	}
	}
}
exit(1);
