@echo off
robocopy .\ E:\Example /MIR /s /z /R:3 /W:10 /LOG+:.\archivo_de_registro.log