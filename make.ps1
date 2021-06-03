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
$app_names["hydro"]  = "Hydro"
$app_names["qfem"] = "quoFEM"
$app_names["pelicun"]  = "pelicun"
$app_names["rtm"] = "requirements"

$formats = @{"html" = "","spell" = ""}

function json-to-csv{
    $QF_Examples = @("-Eqfem") + (gci "$env:SIMCENTER_DEV\quoFEM\Examples\qfem*\src\input.json")
    $EE_Examples = @("-Eeeuq") + (gci "$env:SIMCENTER_DEV\EE-UQ\Examples\eeuq-*\src\input.json")
    $WE_Examples = @("-Eweuq") + (gci "$env:SIMCENTER_DEV\WE-UQ\Examples\weuq-*\src\input.json")
    $PB_Examples = @("-Epbdl") + (gci "$env:SIMCENTER_DEV\PBE\Examples\pbdl-*\src\input.json")
    $R2_Examples = @("-Er2dt") + (gci "$env:SIMCENTER_DEV\R2DTool\Examples\E[0-9]*\input.json")
    $arglist = @("scripts/json2csv.py") + $QF_Examples + $EE_Examples + $WE_Examples + $PB_Examples + $R2_Examples
    write-host $arglist
    Get-ChildItem -File -Filter ".\docs\common\reqments\data\*.json" | ForEach-Object {
        start-process python -ArgumentList $arglist -RedirectStandardOutput ("docs\common\reqments\_out\" + $_.basename + ".csv") -Wait -NoNewWindow -RedirectStandardInput (".\docs\common\reqments\data\" + $_.name)
    }
}

if ($args.count -eq 0){
    # Run old-style build using app from conf.py
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
    json-to-csv 
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


