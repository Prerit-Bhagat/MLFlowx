package com.example.prediction.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.prediction.entity.PredictionEntity;

public interface PredictionRepository extends JpaRepository<PredictionEntity, Long> {
}