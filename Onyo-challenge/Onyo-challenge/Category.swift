//
//  Category.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit

class Category {
    
    // MARK: - Properties
    
    var numericalId: Double!
    var displayName: String?
    var imageMainURL: String?
    
    // MARK: Initialization
    
    init(dict: [String: AnyObject]) {
        numericalId = dict["numericalId"] as! Double
        
        displayName = dict["name"] as? String
        
        if let imageArray = dict["image"] as? [[String: AnyObject]] {
            imageMainURL = imageArray[0]["url"] as? String
        }
        
    }
    
}