package com.example.prediction.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "prediction_entity")
public class PredictionEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "car_year")   // 🔥 FIXED (no reserved keyword)
    private int year;

    private int kmDriven;
    private int prediction;

    // Getters & Setters
    public Long getId() { return id; }

    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }

    public int getKmDriven() { return kmDriven; }
    public void setKmDriven(int kmDriven) { this.kmDriven = kmDriven; }

    public int getPrediction() { return prediction; }
    public void setPrediction(int prediction) { this.prediction = prediction; }
}