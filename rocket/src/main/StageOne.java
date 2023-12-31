package main;

public class StageOne extends Stages {

    public StageOne() {
        t = 135.0; // Время работы первой ступени, с
        F = 34_500_000.0; // Суммарная тяга двигателей первой ступени в ваккууме (4 + 1), Н
        Fmin = 34_500_000.0; // Суммарная тяга двигателей на старте (4 + 1), Н
        M = M0 + M1 + M2 + M3 + Mk + M4; // Стартовая масса ракеты с космическим кораблём, кг
        angle = 65.0; // Конечный угол поворота ракеты относительно вертикальной оси за время работы первой ступени, град
        k = (M1 - M1e)/t;

        calculateTimeValues();
    }

    // flag = 0 - без сопротивления воздуха
    // flag = 1 - с сопротивлением воздуха
    public void calculateFunction(int flag) {
        for(int i = 0; i < timeValues.size(); i++) {
            if(i == 0) {
                Double resistance = (flag)*Resistance.resistance(0.0, 0.0, 0.0, M, k, timeValues.get(i));
                accelerationXValues.add(xFunction(timeValues.get(i), resistance));
                accelerationYValues.add(yFunction(timeValues.get(i), resistance));
                resistanceValues.add(resistance);
            }
            if(i > 0) {
                Double resistance = (flag)*Resistance.resistance(movementYValues.get(i - 1), speedXValues.get(i - 1), speedYValues.get(i - 1), M, k, timeValues.get(i));
                accelerationXValues.add(xFunction(timeValues.get(i), resistance));
                accelerationYValues.add(yFunction(timeValues.get(i), resistance));
                resistanceValues.add(resistance);
            }
            speedXValues.add(euler(setStartValues(speedXValues, null, i), accelerationXValues.get(i)));
            speedYValues.add(euler(setStartValues(speedYValues, null, i), accelerationYValues.get(i)));
            movementXValues.add(euler(setStartValues(movementXValues, null, i), speedXValues.get(i)));
            movementYValues.add(euler(setStartValues(movementYValues, null, i), speedYValues.get(i)));
        }

        printParameters();
    }

    private Double xFunction(Double arg, Double resistance) {
        return (((Fmin + engineForceIncrease()*arg) - resistance) * Math.sin(rotationAngleFunction()*arg))/(M - k*arg);
    }

    private Double yFunction(Double arg, Double resistance) {
        return (((Fmin + engineForceIncrease()*arg) - resistance) * Math.cos(rotationAngleFunction()*arg))/(M - k*arg) - g;
    }

    private Double engineForceIncrease() {
        return (F - Fmin)/t;
    }
}