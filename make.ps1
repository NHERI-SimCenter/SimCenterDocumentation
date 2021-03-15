# Claudio Perez

write-host "0" $args[0] "1" $args[1] "2" $args[2]

if ($env:SPHINXBUILD -eq "") {
	$env:SPHINXBUILD="sphinx-build"
}
$SOURCEDIR="./docs"

if ($args[0] -eq "") {goto help}

$env:SIMCENTER_DEV = resolve-path "../"

$app_names = @{}
$app_names["we"]  = "WE-UQ"
$app_names["ee"]  = "EE-UQ"
$app_names["r2d"]  = "R2DTool"
$app_names["pbe"]  = "PBE"
$app_names["qfem"] = "quoFEM"
$app_names["pelicun"]  = "pelicun"
$app_names["req"] = "requirements"

$formats = @{"html" = ""}

if ($args.count -eq 0){
    start-process sphinx-build -ArgumentList @("-M","help",$SOURCEDIR,$BUILDDIR)  -Wait -NoNewWindow
    #iex $command
    return
}

if ($app_names.ContainsKey($args[0])){
    if ($args.count -lt 2) {
        write-host "No format specified; try running ./make <app-name> html"
        return
    } elseif (-not $formats.containsKey($args[1])) {
        write-host "Format unsupported"
        return
    }
    $app_name = $app_names[$args[0]]
    $format = $args[1]
    $env:SIMDOC_APP = $app_name
    $BUILDDIR="./build/$app_name/$format"
    write-host "Building $app_name $format"
    write-host "  in $BUILDDIR"
    start-process sphinx-build -ArgumentList @("-b",$format,$SOURCEDIR,$BUILDDIR) -Wait -NoNewWindow
    return
}



#%SPHINXBUILD% >NUL 2>NUL
#if (errorlevel 9009) {
#	echo.
#	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
#	echo.installed, then set the SPHINXBUILD environment variable to point
#	echo.to the full path of the 'sphinx-build' executable. Alternatively you
#	echo.may add the Sphinx directory to PATH.
#	echo.
#	echo.If you don't have Sphinx installed, grab it from
#	echo.http://sphinx-doc.org/
#	exit /b 1
#}
#
#%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
#goto end


