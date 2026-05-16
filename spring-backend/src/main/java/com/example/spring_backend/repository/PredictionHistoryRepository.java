package com.example.spring_backend.repository;

import com.example.spring_backend.entity.PredictionHistory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PredictionHistoryRepository
        extends JpaRepository<PredictionHistory, Long> {
}