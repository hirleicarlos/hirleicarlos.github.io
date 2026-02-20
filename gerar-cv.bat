@echo off
title Gerar Curriculo PDF

echo ===============================
echo Gerando Curriculo PDF...
echo ===============================

REM Ir para a pasta do projeto
cd /d C:\laragon\www\hirleicarlos.github.io

REM Executar script Python
python automacao\cv\scripts\build_cv.py

echo.
echo ===============================
echo Processo finalizado.
echo ===============================
echo.

pause