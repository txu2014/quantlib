/* -*- mode: c++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*
 Copyright (C) 2006 Mark Joshi

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/reference/license.html>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
*/


#ifndef quantlib_market_model_parametric_exercise_hpp
#define quantlib_market_model_parametric_exercise_hpp

#include <ql/MarketModels/nodedataprovider.hpp>
#include <ql/MonteCarlo/genericparametricearlyexercise.hpp>
#include <memory>

namespace QuantLib {

    class MarketModelParametricExercise : public MarketModelNodeDataProvider,
                                          public ParametricExercise {
      public:
        std::vector<Size> numberOfData() const {
            return numberOfVariables();
        }
        virtual std::auto_ptr<MarketModelParametricExercise> clone() const = 0;
    };

}


#endif