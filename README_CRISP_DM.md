# 📊 CRISP-DM - Fase 1: Business Understanding

## 🏢 Contexto del Negocio

Una empresa de telecomunicaciones enfrenta una alta tasa de cancelación de clientes (churn), lo que impacta negativamente en sus ingresos y crecimiento.

El churn representa la pérdida de clientes que dejan de utilizar los servicios de la empresa, generando costos adicionales en adquisición de nuevos clientes.

---

## ❗ Problema de Negocio

La empresa no cuenta con un sistema que permita identificar de manera anticipada qué clientes tienen mayor probabilidad de abandonar el servicio.

Esto dificulta la implementación de estrategias de retención efectivas.

---

## 🎯 Objetivo del Proyecto

Desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de churn de un cliente, permitiendo tomar acciones preventivas.

---

## 🎯 Objetivos de Negocio

- Reducir la tasa de churn en al menos un X%
- Identificar clientes en riesgo de abandono
- Optimizar campañas de retención
- Disminuir costos asociados a la pérdida de clientes

---

## 🤖 Traducción a Problema de Machine Learning

- Tipo de problema: Clasificación binaria
- Variable objetivo (target): `Churn`
  - 0 → Cliente permanece
  - 1 → Cliente abandona

---

## 📊 Métricas de Éxito

Dado que el costo de no detectar un cliente que abandonará es alto, se priorizan las siguientes métricas:

- Recall (detección de churn)
- F1-Score
- ROC-AUC

La accuracy no será la métrica principal debido al posible desbalance de clases.

---

## ⚠️ Restricciones

- Disponibilidad de datos históricos
- No uso de datos sensibles
- Calidad de datos variable
- Posible desbalance en la variable objetivo

---

## 💡 Caso de Uso

Ejemplo:

Si el modelo predice que un cliente tiene un 85% de probabilidad de abandonar el servicio:

→ Se pueden activar acciones como:
- Ofrecer descuentos personalizados
- Contacto directo con el cliente
- Beneficios exclusivos

---

## 🚀 Resultado Esperado

Un sistema que permita:

- Predecir churn en tiempo real
- Integrarse con sistemas de negocio
- Facilitar la toma de decisiones estratégicas