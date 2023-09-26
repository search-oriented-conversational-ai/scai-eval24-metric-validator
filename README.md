# SCAI Eval 2024 Metric Validator
This repository contains code for validating metric labels submitted to SCAI Eval 2024

## Local Usage
```bash
python3 scai-eval24-metric-validator.py ground-truth-directory run-directory/run.json /dev/zero
```

## TIRA Usage
Command in TIRA:
```bash
python3 /app/scai-eval24-metric-validator.py $inputDir $inputRun/* $outputDir/evaluation.prototext
```

## Docker
```bash
docker build -t webis/scai-eval24-metric-validator:1.0.0 .
docker push webis/scai-eval24-metric-validator:1.0.0
```

