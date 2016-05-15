//
//  Company.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import MapKit

class Company {
    
    // MARK: - Properties
    
    var numericalId: Double!
    var displayName: String?
    var address: String?
    var imageMainURL: String?
    var coordinates: CLLocation?
    
    // MARK: Initialization
    
    init(dict: [String: AnyObject]) {
        numericalId = dict["numericalId"] as! Double
        
        displayName = dict["displayName"] as? String
        address = dict["address"] as? String
        
        if let imageArray = dict["image"] as? [[String: AnyObject]] {
            if imageArray.count > 2 {
                imageMainURL = imageArray[2]["url"] as? String
            }
        }
        
        if let geoLat = dict["geoLat"] as? String, let geoLon = dict["geoLon"] as? String {
            coordinates = CLLocation(latitude: Double(geoLat)!, longitude: Double(geoLon)!)
        }
       
    }
    
}