@echo off
title Gerar Curriculo PDF

echo ===============================
echo Gerando Curriculo PDF...
echo ===============================

wsl bash -lc "cd /home/hirleicarlos/projetos/hirlei-github-io && python3 automacao/cv/scripts/build_cv.py"

echo.
echo ===============================
echo Processo finalizado.
echo ===============================
echo.

pause