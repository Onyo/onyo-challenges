//
//  NibObjects.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import Foundation

enum NibObjects: String {
    
    case CompanyTableViewCell
    
    static func reuseIdentifierFor(nibTableViewCell: NibObjects) -> String {
        switch nibTableViewCell {
        case .CompanyTableViewCell: return "CompanyCellIdentifier"
        }
    }
    
}