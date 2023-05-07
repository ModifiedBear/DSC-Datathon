# DSC-Datathon

Proyecto para DSC Datathon del equipo _cue-bits_.

## Descripción

Este proyecto tiene como finalidad dar un score de anomalías detectadas dado un instante de tiempo.
El funcionamiento del código se puede ver en los ejemplos: [main](./main.py) o en el iPynb [example](./example.ipynb).

## Funcionamiento

Desarrollamos un `pipeline`, el cual toma los datos del servidor que se quiere analizar (puede ser cualquier servidor).
El input de datos al `pipeline` deben ser datos `resampled`, los cuales se pueden generar la función de `resampling`.

El `pipeline` toma los datos y obtiene los `indicadores`, los cuales se les obtiene de manera global, pero cada punto de `anomalia` en un `indicador` es trackeado en el tiempo. El `pipeline` regresa un score en cada tiempo de que tan anomalo fue ese punto temporal.

## Exploración

La exploración de la base de datos fue hecha en la branch `main`.
