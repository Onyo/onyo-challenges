//
//  LocationManager.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import MapKit

class LocationManager: NSObject {
    
    // MARK; - Properties
    
    var locationManager: CLLocationManager!
    var currentLocation: CLLocation!
    
    // MARK: -- Singleton
    
    class var sharedInstance: LocationManager {
        struct Static {
            static var instance: LocationManager?
            static var token: dispatch_once_t = 0
        }
        
        dispatch_once(&Static.token) {
            Static.instance = LocationManager()
        }
        
        return Static.instance!
    }
    
    // MARK: - Config
    
    func config() {
        locationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }
    
}

extension LocationManager: CLLocationManagerDelegate {
    
    func locationManager(manager: CLLocationManager, didUpdateToLocation newLocation: CLLocation, fromLocation oldLocation: CLLocation) {
        currentLocation = newLocation
    }
    
}